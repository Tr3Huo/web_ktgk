import os

webapp_path = r'D:\Study\NAM3\KY1\DOT1\WEB\Workspace\Web_ktgk\src\main\webapp'
webinf_path = os.path.join(webapp_path, 'WEB-INF')
decorators_path = os.path.join(webinf_path, 'decorators')
views_web_path = os.path.join(webapp_path, 'views', 'web')
views_admin_path = os.path.join(webapp_path, 'views', 'admin')
views_admin_video_path = os.path.join(views_admin_path, 'video')
common_path = os.path.join(webapp_path, 'common')

for p in [decorators_path, views_web_path, views_admin_video_path, common_path]:
    if not os.path.exists(p):
        os.makedirs(p)

jsps = {
    'WEB-INF/web.xml': """<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
         
    <!-- Sitemesh Filter -->
    <filter>
        <filter-name>sitemesh</filter-name>
        <filter-class>com.opensymphony.sitemesh.webapp.SiteMeshFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>sitemesh</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>

</web-app>
""",
    'WEB-INF/decorators.xml': """<?xml version="1.0" encoding="UTF-8"?>
<decorators defaultdir="/common">
    <decorator name="admin" page="admin.jsp">
        <pattern>/admin/*</pattern>
    </decorator>
    <decorator name="web" page="web.jsp">
        <pattern>/*</pattern>
    </decorator>
</decorators>
""",
    'common/admin.jsp': """<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title><sitemesh:write property='title'/></title>
<sitemesh:write property='head'/>
<style>
    body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
    .header { background-color: #333; color: white; padding: 15px; }
    .header a { color: white; text-decoration: none; margin-right: 15px; }
    .content { padding: 20px; min-height: 400px; }
    .footer { background-color: #333; color: white; text-align: center; padding: 15px; position: fixed; bottom: 0; width: 100%; }
</style>
</head>
<body>
    <div class="header">
        <a href="${pageContext.request.contextPath}/home">Trang Chủ</a>
        <a href="${pageContext.request.contextPath}/home">Sản phẩm</a>
        <a href="${pageContext.request.contextPath}/admin/home">Trang quản trị</a>
        <a href="${pageContext.request.contextPath}/logout">Đăng xuất</a>
    </div>
    
    <div class="content">
        <sitemesh:write property='body'/>
    </div>
    
    <div class="footer">
        Họ tên: User_Name - MSSV: 24110232 - Mã đề: 03
    </div>
</body>
</html>
""",
    'common/web.jsp': """<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title><sitemesh:write property='title'/></title>
<sitemesh:write property='head'/>
<style>
    body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
    .header { background-color: #007bff; color: white; padding: 15px; }
    .header a { color: white; text-decoration: none; margin-right: 15px; }
    .content { padding: 20px; min-height: 400px; margin-bottom: 50px; }
    .footer { background-color: #007bff; color: white; text-align: center; padding: 15px; position: fixed; bottom: 0; width: 100%; }
</style>
</head>
<body>
    <div class="header">
        <a href="${pageContext.request.contextPath}/home">Trang Chủ</a>
        <a href="${pageContext.request.contextPath}/home">Sản phẩm</a>
        <c:choose>
            <c:when test="${sessionScope.account != null}">
                <c:if test="${sessionScope.account.admin == true}">
                    <a href="${pageContext.request.contextPath}/admin/home">Trang quản trị</a>
                </c:if>
                <a href="${pageContext.request.contextPath}/logout">Đăng xuất</a>
            </c:when>
            <c:otherwise>
                <a href="${pageContext.request.contextPath}/login">Đăng nhập</a>
            </c:otherwise>
        </c:choose>
    </div>
    
    <div class="content">
        <sitemesh:write property='body'/>
    </div>
    
    <div class="footer">
        Họ tên: Nhựt Hùng - MSSV: 24110232 - Mã đề: 03
    </div>
</body>
</html>
""",
    'views/web/login.jsp': """<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
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
""",
    'views/web/register.jsp': """<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<head>
    <title>Đăng ký</title>
</head>
<body>
    <h2>Đăng ký tài khoản</h2>
    <p style="color:red;">${message}</p>
    <form action="${pageContext.request.contextPath}/register" method="post">
        <label>Tên đăng nhập:</label><br>
        <input type="text" name="username" required><br><br>
        <label>Họ và tên:</label><br>
        <input type="text" name="fullname" required><br><br>
        <label>Email:</label><br>
        <input type="email" name="email" required><br><br>
        <label>Mật khẩu:</label><br>
        <input type="password" name="password" required><br><br>
        <input type="submit" value="Đăng ký">
    </form>
</body>
""",
    'views/web/verify-otp.jsp': """<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
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
""",
    'views/web/home.jsp': """<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
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
    <h2>Danh mục Video</h2>
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
                    <img src="${video.poster}" alt="Poster" style="width:100px; height:100px; background-color:#eee;"><br>
                    <strong>Tiêu đề: ${video.title}</strong><br>
                    Mã video: ${video.videoId}<br>
                    Category name: ${video.category.categoryname}<br>
                    View: ${video.views}<br>
                    Share(10)<br>
                    Like(10)<br>
                    <a href="${pageContext.request.contextPath}/video-detail?id=${video.videoId}">Xem chi tiết</a>
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
""",
    'views/web/video-detail.jsp': """<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
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
    <div class="detail-container">
        <div class="poster">
            <c:choose>
                <c:when test="${not empty video.poster}">
                    <img src="${video.poster}" alt="Poster" style="max-width:100%; max-height:100%;">
                </c:when>
                <c:otherwise>
                    [poster]
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
        </div>
    </div>
    <div class="desc">
        <p>description: ${video.description}</p>
    </div>
</body>
""",
    'views/admin/home.jsp': """<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<head>
    <title>Trang quản trị</title>
</head>
<body>
    <h2>Chào mừng đến với trang quản trị</h2>
    <ul>
        <li><a href="${pageContext.request.contextPath}/admin/video">Quản lý Video</a></li>
    </ul>
</body>
""",
    'views/admin/video/list.jsp': """<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
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
            <th>Title</th>
            <th>Views</th>
            <th>Active</th>
            <th>Category</th>
            <th>Action</th>
        </tr>
        <c:forEach items="${videos}" var="video">
            <tr>
                <td>${video.videoId}</td>
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
""",
    'views/admin/video/add.jsp': """<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<head>
    <title>Thêm Video</title>
</head>
<body>
    <h2>Thêm Video mới</h2>
    <form action="${pageContext.request.contextPath}/admin/video/add" method="post">
        <label>Video ID:</label><br>
        <input type="text" name="videoId" required><br><br>
        <label>Title:</label><br>
        <input type="text" name="title" required><br><br>
        <label>Description:</label><br>
        <textarea name="description"></textarea><br><br>
        <label>Poster (URL):</label><br>
        <input type="text" name="poster"><br><br>
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
""",
    'views/admin/video/edit.jsp': """<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<head>
    <title>Cập nhật Video</title>
</head>
<body>
    <h2>Cập nhật Video</h2>
    <form action="${pageContext.request.contextPath}/admin/video/edit" method="post">
        <label>Video ID:</label><br>
        <input type="text" name="videoId" value="${video.videoId}" readonly><br><br>
        <label>Title:</label><br>
        <input type="text" name="title" value="${video.title}" required><br><br>
        <label>Description:</label><br>
        <textarea name="description">${video.description}</textarea><br><br>
        <label>Poster (URL):</label><br>
        <input type="text" name="poster" value="${video.poster}"><br><br>
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
"""
}

for name, content in jsps.items():
    with open(os.path.join(webapp_path, name), 'w', encoding='utf-8') as f:
        f.write(content)

print("JSPs created.")
