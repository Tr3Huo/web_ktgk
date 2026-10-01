<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>
<head>
    <title>Trang Chủ</title>
    <style>
        .video-container { display: flex; flex-wrap: wrap; }
        .video-item { border: 1px solid #ccc; margin: 10px; padding: 10px; width: 30%; text-align: center; }
        .video-item img { max-width: 100%; height: auto; }
        .pagination { margin-top: 20px; }
        .pagination a { padding: 5px 10px; margin: 0 5px; border: 1px solid #007bff; text-decoration: none; }
    </style>
</head>
<body>
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <h2>Danh mục Video</h2>
        <a href="${pageContext.request.contextPath}/cart" style="padding: 10px; background-color: #28a745; color: white; text-decoration: none; border-radius: 5px;">
            🛒 Xem giỏ hàng (<c:out value="${sessionScope.cart != null ? sessionScope.cart.size() : 0}" />)
        </a>
    </div>
    <div>
        <c:forEach items="${categories}" var="cat">
            <a href="?catId=${cat.categoryId}" style="margin-right: 15px;">${cat.categoryname}</a>
        </c:forEach>
    </div>
    
    <hr>
    
    <c:if test="${not empty catId}">
        <h3>Category Name (${count})</h3>
        <div class="video-container">
            <c:forEach items="${videos}" var="video">
                <div class="video-item">
                    <c:choose>
                        <c:when test="${not empty video.poster and fn:trim(video.poster) != ''}">
                            <img src="${video.poster}" alt="Poster" style="width:100px; height:100px; background-color:#eee; object-fit: cover;"><br>
                        </c:when>
                        <c:otherwise>
                            <img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22150%22%20height%3D%22150%22%20viewBox%3D%220%200%20150%20150%22%3E%3Crect%20fill%3D%22%23dddddd%22%20width%3D%22150%22%20height%3D%22150%22%2F%3E%3Ctext%20fill%3D%22%23888888%22%20font-family%3D%22sans-serif%22%20font-size%3D%2216%22%20dy%3D%225%22%20font-weight%3D%22bold%22%20x%3D%2250%25%22%20y%3D%2250%25%22%20text-anchor%3D%22middle%22%3EVideo%3C%2Ftext%3E%3C%2Fsvg%3E" alt="Poster" style="width:100px; height:100px; background-color:#eee; object-fit: cover;"><br>
                        </c:otherwise>
                    </c:choose>
                    <strong>Tiêu đề: ${video.title}</strong><br>
                    Mã video: ${video.videoId}<br>
                    Category name: ${video.category.categoryname}<br>
                    View: ${video.views}<br>
                    Share(10)<br>
                    Like(10)<br>
                    <a href="${pageContext.request.contextPath}/video-detail?id=${video.videoId}">Xem chi tiết</a> | 
                    <a href="${pageContext.request.contextPath}/cart/add?videoId=${video.videoId}" style="color: green; text-decoration: none; font-weight: bold;">+ Thêm vào giỏ</a>
                </div>
            </c:forEach>
        </div>
        
        <div class="pagination">
            << 
            <c:forEach begin="1" end="${endPage}" var="i">
                <a href="?catId=${catId}&page=${i}">${i}</a>
            </c:forEach>
            >>
        </div>
    </c:if>
</body>
