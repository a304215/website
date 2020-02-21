<?php
    $error_message = "";
    $account = $_POST[account];
    $password = $_POST[password];
    $passwordCheck = $_POST[passwordCheck];
    $email = $_POST[email];
    $address = $_POST[address];
    $school = $_POST[school];
    $department = $_POST[department];
    $age = $_POST[age];
    $birthDay = $_POST[birthDay];
    $chineseFirstName = $_POST[chineseFirstName];
    $chineseLastName = $_POST[chineseLastName];
    $englishFirstName = $_POST[englishFirstName];
    $englishLastName = $_POST[englishLastName];
    $language = $_POST[language];
    $skill = $_POST[skill];
    echo "資料輸入成功";
    $conn = mysqli_connect("server_pin","account","password","db");
    mysqli_query($conn,"SET NAME UTF-8");
?>