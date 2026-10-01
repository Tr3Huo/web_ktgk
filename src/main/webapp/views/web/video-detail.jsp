<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>
<head>
    <title>Chi tiết Video</title>
    <style>
        .detail-container { display: flex; border: 1px solid #ccc; padding: 20px; }
        .poster { width: 300px; height: 300px; background-color: #eee; margin-right: 20px; text-align: center; line-height: 300px; }
        .info { flex-grow: 1; }
        .desc { margin-top: 20px; border-top: 1px solid #ccc; padding-top: 10px; }
    </style>
</head>
<body>
    <div style="text-align: right; padding: 10px;">
        <a href="${pageContext.request.contextPath}/cart" style="padding: 10px; background-color: #28a745; color: white; text-decoration: none; border-radius: 5px;">
            🛒 Xem giỏ hàng (<c:out value="${sessionScope.cart != null ? sessionScope.cart.size() : 0}" />)
        </a>
    </div>
    <div class="detail-container">
        <div class="poster">
            <c:choose>
                <c:when test="${not empty video.poster and fn:trim(video.poster) != ''}">
                    <img src="${video.poster}" alt="Poster" style="max-width:100%; max-height:100%;">
                </c:when>
                <c:otherwise>
                    <img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22300%22%20height%3D%22300%22%20viewBox%3D%220%200%20300%20300%22%3E%3Crect%20fill%3D%22%23dddddd%22%20width%3D%22300%22%20height%3D%22300%22%2F%3E%3Ctext%20fill%3D%22%23888888%22%20font-family%3D%22sans-serif%22%20font-size%3D%2224%22%20dy%3D%228%22%20font-weight%3D%22bold%22%20x%3D%2250%25%22%20y%3D%2250%25%22%20text-anchor%3D%22middle%22%3EVideo%3C%2Ftext%3E%3C%2Fsvg%3E" alt="Poster" style="max-width:100%; max-height:100%;">
                </c:otherwise>
            </c:choose>
        </div>
        <div class="info">
            <h2>Tiêu đề: ${video.title}</h2>
            <p>Mã video: ${video.videoId}</p>
            <p>Category name: ${video.category.categoryname}</p>
            <p>View: ${video.views}</p>
            <p>Share(10)</p>
            <p>Like(10)</p>
            <div style="margin-top: 20px;">
                <a href="${pageContext.request.contextPath}/cart/add?videoId=${video.videoId}" style="padding: 10px 15px; background-color: #28a745; color: white; text-decoration: none; border-radius: 5px; font-weight: bold;">
                    + Thêm vào giỏ hàng
                </a>
            </div>
        </div>
    </div>
    <div class="desc">
        <p>description: ${video.description}</p>
    </div>
</body>
