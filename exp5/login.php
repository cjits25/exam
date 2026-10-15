<html>
<head>
    <title>Simple Login</title>
    <style>
        body {
            font-family: Arial;
            background: #f3f3f3;
        }
        .login-box {
            width: 300px;
            margin: 100px auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px gray;
        }
        input[type=text], input[type=password] {
            width: 100%;
            padding: 8px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type=submit] {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border: none;
            cursor: pointer;
            width: 100%;
            border-radius: 4px;
        }
        input[type=submit]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
<div class="login-box">
    <h2>Login Form</h2>
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username" required>
        <label>Password:</label>
        <input type="password" name="password" required>
        <input type="submit" name="login" value="Login">
    </form>

    <?php
    if (isset($_POST['login'])) {
        $username = $_POST['username'];
        $password = $_POST['password'];

        // Simple hardcoded check
        if ($username == "admin" && $password == "12345") {
            echo "<p style='color:green;'>Login Successful!</p>";
        } else {
            echo "<p style='color:red;'>Invalid Username or Password</p>";
        }
    }
    ?>
</div>
</body>
</html>
