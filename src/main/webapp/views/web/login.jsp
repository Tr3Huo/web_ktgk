<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<head>
    <title>Đăng nhập</title>
</head>
<body>
    <h2>Đăng nhập</h2>
    <p style="color:red;">${message}</p>
    <form action="${pageContext.request.contextPath}/login" method="post">
        <label>Tên đăng nhập:</label><br>
        <input type="text" name="username" required><br><br>
        <label>Mật khẩu:</label><br>
        <input type="password" name="password" required><br><br>
        <input type="submit" value="Đăng nhập">
    </form>
    <br>
    <a href="${pageContext.request.contextPath}/register">Đăng ký tài khoản mới</a>
</body>
