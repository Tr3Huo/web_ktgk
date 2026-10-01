<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<head>
    <title>Cập nhật Video</title>
</head>
<body>
    <h2>Cập nhật Video</h2>
    <form action="${pageContext.request.contextPath}/admin/video/edit" method="post" enctype="multipart/form-data">
        <label>Video ID:</label><br>
        <input type="text" name="videoId" value="${video.videoId}" readonly><br><br>
        <label>Title:</label><br>
        <input type="text" name="title" value="${video.title}" required><br><br>
        <label>Description:</label><br>
        <textarea name="description">${video.description}</textarea><br><br>
        <label>Poster (File mới):</label><br>
        <input type="file" name="poster"><br><br>
        <label>Views:</label><br>
        <input type="number" name="views" value="${video.views}"><br><br>
        <label>Active:</label><br>
        <input type="radio" name="active" value="true" ${video.active ? 'checked' : ''}> Có
        <input type="radio" name="active" value="false" ${!video.active ? 'checked' : ''}> Không<br><br>
        <label>Category:</label><br>
        <select name="categoryId">
            <c:forEach items="${categories}" var="cat">
                <option value="${cat.categoryId}" ${cat.categoryId == video.category.categoryId ? 'selected' : ''}>${cat.categoryname}</option>
            </c:forEach>
        </select><br><br>
        <input type="submit" value="Lưu">
    </form>
</body>
