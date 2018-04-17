package apoorva.mycalculator;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.math.BigDecimal;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    Button add, subtract, multiply, divide, sin, cos, tan, clear, memadd, memsub, memread, memclr;
    TextView result;
    EditText num1, num2;

    double ans = 0.0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        init();
    }

    public void init() {
        add = (Button)findViewById(R.id.add);
        subtract = (Button)findViewById(R.id.subtract);
        multiply = (Button)findViewById(R.id.multiply);
        divide = (Button)findViewById(R.id.divide);
        sin = (Button)findViewById(R.id.sine);
        cos = (Button)findViewById(R.id.cos);
        tan = (Button)findViewById(R.id.tan);
        clear = (Button)findViewById(R.id.clear);
        memadd = (Button)findViewById(R.id.memadd);
        memsub = (Button)findViewById(R.id.memsub);
        memread = (Button)findViewById(R.id.memread);
        memclr = (Button)findViewById(R.id.memclr);

        num1 = (EditText)findViewById(R.id.num1);
        num2 = (EditText)findViewById(R.id.num2);

        result = (TextView)findViewById(R.id.result);

        add.setOnClickListener(this);
        subtract.setOnClickListener(this);
        multiply.setOnClickListener(this);
        divide.setOnClickListener(this);
        sin.setOnClickListener(this);
        cos.setOnClickListener(this);
        tan.setOnClickListener(this);
        clear.setOnClickListener(this);
        memadd.setOnClickListener(this);
        memsub.setOnClickListener(this);
        memread.setOnClickListener(this);
        memclr.setOnClickListener(this);
    }

    @Override
    public void onClick(View v){

        String a, b;


        switch (v.getId()){

            case R.id.add:
                            a = num1.getText().toString();
                            b = num2.getText().toString();
                            ans = Double.parseDouble(a) + Double.parseDouble(b);
                            result.setText(String.valueOf(ans));
                            break;

            case R.id.subtract:
                            a = num1.getText().toString();
                            b = num2.getText().toString();
                            ans = Double.parseDouble(a) - Double.parseDouble(b);
                            result.setText(String.valueOf(ans));
                            break;

            case R.id.multiply:
                 a = num1.getText().toString();
                 b = num2.getText().toString();
                            ans = Double.parseDouble(a) * Double.parseDouble(b);
                            result.setText(String.valueOf(ans));
                            break;

            case R.id.divide:
                a = num1.getText().toString();
                b = num2.getText().toString();
                            try{
                                BigDecimal a1 = new BigDecimal(Double.parseDouble(a));
                                BigDecimal b1 = new BigDecimal(Double.parseDouble(b));
                                BigDecimal div_ans = a1.divide(b1,5,BigDecimal.ROUND_HALF_UP);
                                result.setText(String.valueOf(div_ans));
                            }
                            catch (Exception e){
                                result.setText("Cannot Divide by zero!");
                            }
                            break;

            case R.id.sine:
                 a = num1.getText().toString();
                            num2.setText(" ");
                            ans = Math.sin(Double.parseDouble(a));
                            result.setText(String.valueOf(ans));
                            break;
            case R.id.cos:
                 a = num1.getText().toString();
                            num2.setText(" ");
                            ans = Math.cos(Double.parseDouble(a));
                            result.setText(String.valueOf(ans));
                            break;
            case R.id.tan:
                 a = num1.getText().toString();
                            num2.setText(" ");
                            ans = Math.tan(Double.parseDouble(a));
                            result.setText(String.valueOf(ans));
                            break;

            case R.id.clear:
                            num1.setText(" ");
                            num2.setText(" ");
                            result.setText("Result");
                            break;

            case R.id.memadd:
                            b = num2.getText().toString();
                            num1.setText(" "+String.valueOf(ans));
                            ans+=Double.parseDouble(b);
                            result.setText(String.valueOf(ans));

            case R.id.memsub:
                            b = num2.getText().toString();
                            num1.setText(" "+String.valueOf(ans));
                            ans-=Double.parseDouble(b);
                            result.setText(String.valueOf(ans));

            case R.id.memread:
                            num1.setText(" ");
                            num2.setText(" ");
                            result.setText(String.valueOf(ans));

            case R.id.memclr:
                            num1.setText(" ");
                            num2.setText(" ");
                            ans = 0;
                            result.setText("Result");

        }
    }
}
