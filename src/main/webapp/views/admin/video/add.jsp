<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<head>
    <title>Thêm Video</title>
</head>
<body>
    <h2>Thêm Video mới</h2>
    <form action="${pageContext.request.contextPath}/admin/video/add" method="post" enctype="multipart/form-data">
        <label>Video ID:</label><br>
        <input type="text" name="videoId" required><br><br>
        <label>Title:</label><br>
        <input type="text" name="title" required><br><br>
        <label>Description:</label><br>
        <textarea name="description"></textarea><br><br>
        <label>Poster (File):</label><br>
        <input type="file" name="poster"><br><br>
        <label>Views:</label><br>
        <input type="number" name="views" value="0"><br><br>
        <label>Active:</label><br>
        <input type="radio" name="active" value="true" checked> Có
        <input type="radio" name="active" value="false"> Không<br><br>
        <label>Category:</label><br>
        <select name="categoryId">
            <c:forEach items="${categories}" var="cat">
                <option value="${cat.categoryId}">${cat.categoryname}</option>
            </c:forEach>
        </select><br><br>
        <input type="submit" value="Lưu">
    </form>
</body>
