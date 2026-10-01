<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Thanh Toán (COD)</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .checkout-container { max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ccc; border-radius: 5px; }
        .form-group { margin-bottom: 15px; }
        .form-group label { display: block; font-weight: bold; margin-bottom: 5px; }
        .form-group input, .form-group textarea, .form-group select { width: 100%; padding: 8px; box-sizing: border-box; }
        .btn { padding: 10px 15px; background: #28a745; color: white; border: none; border-radius: 3px; cursor: pointer; font-size: 16px; width: 100%; }
        .btn:hover { background: #218838; }
        .error { color: red; margin-bottom: 15px; }
    </style>
</head>
<body>
    <div class="checkout-container">
        <h2>Thông tin thanh toán</h2>
        
        <c:if test="${not empty error}">
            <div class="error">${error}</div>
        </c:if>
        
        <p>Bạn có <strong>${sessionScope.cart.size()}</strong> sản phẩm trong giỏ.</p>
        
        <form action="${pageContext.request.contextPath}/checkout" method="post">
            <div class="form-group">
                <label>Họ và tên người nhận</label>
                <input type="text" name="customerName" required>
            </div>
            
            <div class="form-group">
                <label>Số điện thoại</label>
                <input type="text" name="phone" required>
            </div>
            
            <div class="form-group">
                <label>Địa chỉ giao hàng</label>
                <textarea name="address" rows="3" required></textarea>
            </div>
            
            <div class="form-group">
                <label>Phương thức thanh toán</label>
                <select name="paymentMethod" required>
                    <option value="COD">Thanh toán khi nhận hàng (COD)</option>
                </select>
            </div>
            
            <button type="submit" class="btn">Xác nhận đặt hàng</button>
            
            <div style="text-align: center; margin-top: 15px;">
                <a href="${pageContext.request.contextPath}/cart">Quay lại giỏ hàng</a>
            </div>
        </form>
    </div>
</body>
</html>
