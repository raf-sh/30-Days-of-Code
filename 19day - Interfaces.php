<?php
interface AdvancedArithmetic {
    public function divisorSum($n);
}
//Write your code here
class Calculator implements AdvancedArithmetic {
    public function divisorSum($n) {
		if (!$this->checkInput($n)) {
			return 0;
		}
		
	    $divisors = [];

	    for ($i = 1; $i < $n; $i++) {
	        if (($n % $i) == 0) {
        	    $divisors[] = $i;
	        }
   		}

		$divisors[] = $n;

		return array_sum($divisors); 
    }
	
	private function checkInput($n) {
		if ($n >= 1 && $n<=1000) {
			return true;
		}
		
		return false;
	}
}

$n=intval(fgets(STDIN));
$myCalculator=new Calculator();

if ($myCalculator instanceof AdvancedArithmetic) {
    $sum=$myCalculator->divisorSum($n);
    echo "I implemented: AdvancedArithmetic\n".$sum;
} else {
    echo "Wrong answer";// You will get this output if you dont implement
}
?>
