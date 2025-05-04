function sortByLength($toSort) {
  usort($toSort, function($a, $b) {
    return strlen($a) - strlen($b);
  });
  return $toSort;
}
