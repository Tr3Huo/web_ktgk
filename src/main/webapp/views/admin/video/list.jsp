<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>
<head>
    <title>Quản lý Video</title>
    <style>
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h2>Danh sách Video</h2>
    <p style="color:green;">${message}</p>
    <a href="${pageContext.request.contextPath}/admin/video/add">Thêm Video mới</a>
    <br><br>
    <table>
        <tr>
            <th>Video ID</th>
            <th>Hình ảnh</th>
            <th>Title</th>
            <th>Views</th>
            <th>Active</th>
            <th>Category</th>
            <th>Action</th>
        </tr>
        <c:forEach items="${videos}" var="video">
            <tr>
                <td>${video.videoId}</td>
                <td>
                    <c:choose>
                        <c:when test="${not empty video.poster and fn:trim(video.poster) != ''}">
                            <img src="${video.poster}" alt="Poster" style="width: 80px; height: 80px; object-fit: cover;">
                        </c:when>
                        <c:otherwise>
                            <img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2280%22%20height%3D%2280%22%20viewBox%3D%220%200%2080%2080%22%3E%3Crect%20fill%3D%22%23dddddd%22%20width%3D%2280%22%20height%3D%2280%22%2F%3E%3Ctext%20fill%3D%22%23888888%22%20font-family%3D%22sans-serif%22%20font-size%3D%2212%22%20dy%3D%224%22%20font-weight%3D%22bold%22%20x%3D%2250%25%22%20y%3D%2250%25%22%20text-anchor%3D%22middle%22%3EVideo%3C%2Ftext%3E%3C%2Fsvg%3E" alt="Poster" style="width: 80px; height: 80px; object-fit: cover;">
                        </c:otherwise>
                    </c:choose>
                </td>
                <td>${video.title}</td>
                <td>${video.views}</td>
                <td>${video.active ? 'Có' : 'Không'}</td>
                <td>${video.category.categoryname}</td>
                <td>
                    <a href="${pageContext.request.contextPath}/admin/video/edit?id=${video.videoId}">Sửa</a> | 
                    <a href="${pageContext.request.contextPath}/admin/video/delete?id=${video.videoId}" onclick="return confirm('Bạn có chắc chắn muốn xóa?');">Xóa</a>
                </td>
            </tr>
        </c:forEach>
    </table>
    
    <div style="margin-top:20px;">
        Phân trang: 
        <c:forEach begin="1" end="${endPage}" var="i">
            <a href="?page=${i}">${i}</a>
        </c:forEach>
    </div>
</body>
