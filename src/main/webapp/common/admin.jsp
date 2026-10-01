<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="decorator" uri="http://www.opensymphony.com/sitemesh/decorator" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title><decorator:title default="Trang Quản Trị" /></title>
<decorator:head />
<style>
    body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
    .header { background-color: #333; color: white; padding: 15px; }
    .header a { color: white; text-decoration: none; margin-right: 15px; }
    .content { padding: 20px; min-height: 400px; }
    .footer { background-color: #333; color: white; text-align: center; padding: 15px; position: fixed; bottom: 0; width: 100%; }
</style>
</head>
<body>
    <div class="header" style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <a href="${pageContext.request.contextPath}/home">Trang Chủ</a>
            <a href="${pageContext.request.contextPath}/products">Sản phẩm</a>
            <a href="${pageContext.request.contextPath}/admin/home">Trang quản trị</a>
            <a href="${pageContext.request.contextPath}/logout">Đăng xuất</a>
        </div>
        <c:if test="${sessionScope.account != null}">
            <div style="font-weight: bold;">
                Xin chào, ${sessionScope.account.fullname}
            </div>
        </c:if>
    </div>
    
    <div class="content">
        <decorator:body />
    </div>
    
    <div class="footer">
        Họ tên: Nhựt Hưng - MSSV: 24110232 - Mã đề: 03
    </div>
</body>
</html>
