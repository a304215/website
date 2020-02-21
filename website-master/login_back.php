<?php
    $account = $_REQUEST["login_account"];
    $password = $_REQUEST["login_password"];
    $conn = mysqli_connect("localhost","root","","member");
    $sql = "SELECT * FROM account_passwd";
    $data = mysqli_query($conn,$sql);
    for($i = 0;i<mysqli_nums_row($data);$i++){
        $result = mysqli_fetch_row($data);
        if($result[0]==$account){
            if($result[1] == $password){
                header("Location: homepage.html");              
            }
        }
    }
    echo "帳號或密碼錯誤";
?>