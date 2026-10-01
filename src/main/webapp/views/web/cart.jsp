<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Giỏ hàng</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ccc; padding: 10px; text-align: center; }
        th { background-color: #f4f4f4; }
        .cart-img { width: 80px; height: 80px; object-fit: cover; }
        .btn { padding: 5px 10px; text-decoration: none; border: 1px solid #007bff; background: #007bff; color: white; border-radius: 3px; cursor: pointer; }
        .btn-danger { background: #dc3545; border-color: #dc3545; }
        .qty-input { width: 60px; text-align: center; }
        .actions { display: flex; gap: 5px; justify-content: center; }
    </style>
</head>
<body>
    <h2>Giỏ hàng của bạn</h2>
    <a href="${pageContext.request.contextPath}/products" class="btn">Tiếp tục xem</a>

    <c:if test="${empty sessionScope.cart or sessionScope.cart.size() == 0}">
        <p>Giỏ hàng trống.</p>
    </c:if>

    <c:if test="${not empty sessionScope.cart and sessionScope.cart.size() > 0}">
        <table>
            <thead>
                <tr>
                    <th>Hình ảnh</th>
                    <th>Tên Video</th>
                    <th>Số lượng</th>
                    <th>Thao tác</th>
                </tr>
            </thead>
            <tbody>
                <c:forEach items="${sessionScope.cart}" var="entry">
                    <c:set var="item" value="${entry.value}" />
                    <tr>
                        <td>
                            <c:choose>
                                <c:when test="${not empty item.video.poster and fn:trim(item.video.poster) != ''}">
                                    <img src="${item.video.poster}" alt="Poster" class="cart-img">
                                </c:when>
                                <c:otherwise>
                                    <img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22150%22%20height%3D%22150%22%20viewBox%3D%220%200%20150%20150%22%3E%3Crect%20fill%3D%22%23dddddd%22%20width%3D%22150%22%20height%3D%22150%22%2F%3E%3Ctext%20fill%3D%22%23888888%22%20font-family%3D%22sans-serif%22%20font-size%3D%2216%22%20dy%3D%225%22%20font-weight%3D%22bold%22%20x%3D%2250%25%22%20y%3D%2250%25%22%20text-anchor%3D%22middle%22%3EVideo%3C%2Ftext%3E%3C%2Fsvg%3E" alt="Poster" class="cart-img">
                                </c:otherwise>
                            </c:choose>
                        </td>
                        <td>${item.video.title}</td>
                        <td>
                            <form action="${pageContext.request.contextPath}/cart/update" method="post" style="display:inline;">
                                <input type="hidden" name="videoId" value="${item.video.videoId}">
                                <input type="number" name="quantity" value="${item.quantity}" min="1" max="100" class="qty-input">
                                <button type="submit" class="btn">Cập nhật</button>
                            </form>
                        </td>
                        <td>
                            <a href="${pageContext.request.contextPath}/cart/remove?videoId=${item.video.videoId}" class="btn btn-danger" onclick="return confirm('Bạn có chắc muốn xóa khỏi giỏ hàng?');">Xóa</a>
                        </td>
                    </tr>
                </c:forEach>
            </tbody>
        </table>
        
        <div style="text-align: right; margin-top: 20px;">
            <a href="${pageContext.request.contextPath}/checkout" class="btn" style="padding: 10px 20px; font-size: 16px; background-color: #28a745; border-color: #28a745;">Thanh toán (COD)</a>
        </div>
    </c:if>
</body>
</html>
