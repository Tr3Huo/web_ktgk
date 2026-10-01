<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Đặt Hàng Thành Công</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        .success-box { display: inline-block; padding: 30px; border: 2px solid #28a745; border-radius: 10px; background-color: #f8fff9; }
        h1 { color: #28a745; }
        a.btn { display: inline-block; margin-top: 20px; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; }
        a.btn:hover { background: #0056b3; }
    </style>
</head>
<body>
    <div class="success-box">
        <h1>🎉 Chúc mừng!</h1>
        <p style="font-size: 18px;">${message}</p>
        <p>Chúng tôi sẽ sớm liên hệ với bạn để xác nhận đơn hàng theo phương thức COD.</p>
        
        <a href="${pageContext.request.contextPath}/products" class="btn">Tiếp tục mua sắm</a>
    </div>
</body>
</html>
