<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<head>
    <title>Xác nhận OTP</title>
</head>
<body>
    <h2>Xác nhận mã OTP</h2>
    <p>Mã OTP đã được gửi về email của bạn.</p>
    <p style="color:red;">${message}</p>
    <form action="${pageContext.request.contextPath}/verify-otp" method="post">
        <label>Nhập mã OTP:</label><br>
        <input type="text" name="otp" required><br><br>
        <input type="submit" value="Xác nhận">
    </form>
</body>
