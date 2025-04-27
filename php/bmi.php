function bmi($weight, $height) {
  $bmi = $weight / ($height * $height);
  return match (true) {
      $bmi <= 18.5 => "Underweight",
      $bmi <= 25.0 => "Normal",
      $bmi <= 30.0 => "Overweight",
      default => "Obese",
  };
}