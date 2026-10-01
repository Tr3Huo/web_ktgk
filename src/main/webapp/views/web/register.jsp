<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<head>
    <title>Đăng ký</title>
</head>
<body>
    <h2>Đăng ký tài khoản</h2>
    <p style="color:red;">${message}</p>
    <form action="${pageContext.request.contextPath}/register" method="post">
        <label>Tên đăng nhập:</label><br>
        <input type="text" name="username" required><br><br>
        <label>Họ và tên:</label><br>
        <input type="text" name="fullname" required><br><br>
        <label>Email:</label><br>
        <input type="email" name="email" required><br><br>
        <label>Mật khẩu:</label><br>
        <input type="password" name="password" required><br><br>
        <input type="submit" value="Đăng ký">
    </form>
</body>
