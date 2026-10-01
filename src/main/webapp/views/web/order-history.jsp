<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>

<div class="container" style="max-width: 1000px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
    <h2>Lịch sử đơn hàng</h2>
    
    <div style="margin-bottom: 20px; display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="${pageContext.request.contextPath}/orders" 
           style="padding: 8px 15px; border-radius: 5px; text-decoration: none; ${currentStatus == null ? 'background: #007bff; color: white;' : 'background: #e9ecef; color: black;'}">
           Tất cả
        </a>
        <a href="${pageContext.request.contextPath}/orders?status=0" 
           style="padding: 8px 15px; border-radius: 5px; text-decoration: none; ${currentStatus == 0 ? 'background: #007bff; color: white;' : 'background: #e9ecef; color: black;'}">
           Đơn hàng mới
        </a>
        <a href="${pageContext.request.contextPath}/orders?status=1" 
           style="padding: 8px 15px; border-radius: 5px; text-decoration: none; ${currentStatus == 1 ? 'background: #007bff; color: white;' : 'background: #e9ecef; color: black;'}">
           Đã xác nhận
        </a>
        <a href="${pageContext.request.contextPath}/orders?status=2" 
           style="padding: 8px 15px; border-radius: 5px; text-decoration: none; ${currentStatus == 2 ? 'background: #007bff; color: white;' : 'background: #e9ecef; color: black;'}">
           Chuẩn bị hàng
        </a>
        <a href="${pageContext.request.contextPath}/orders?status=3" 
           style="padding: 8px 15px; border-radius: 5px; text-decoration: none; ${currentStatus == 3 ? 'background: #007bff; color: white;' : 'background: #e9ecef; color: black;'}">
           Vận chuyển
        </a>
        <a href="${pageContext.request.contextPath}/orders?status=4" 
           style="padding: 8px 15px; border-radius: 5px; text-decoration: none; ${currentStatus == 4 ? 'background: #007bff; color: white;' : 'background: #e9ecef; color: black;'}">
           Giao hàng
        </a>
        <a href="${pageContext.request.contextPath}/orders?status=5" 
           style="padding: 8px 15px; border-radius: 5px; text-decoration: none; ${currentStatus == 5 ? 'background: #007bff; color: white;' : 'background: #e9ecef; color: black;'}">
           Đã giao
        </a>
        <a href="${pageContext.request.contextPath}/orders?status=6" 
           style="padding: 8px 15px; border-radius: 5px; text-decoration: none; ${currentStatus == 6 ? 'background: #007bff; color: white;' : 'background: #e9ecef; color: black;'}">
           Đơn hàng hủy
        </a>
        <a href="${pageContext.request.contextPath}/orders?status=7" 
           style="padding: 8px 15px; border-radius: 5px; text-decoration: none; ${currentStatus == 7 ? 'background: #007bff; color: white;' : 'background: #e9ecef; color: black;'}">
           Đơn hàng hoàn
        </a>
    </div>

    <table style="width: 100%; border-collapse: collapse; text-align: left;">
        <thead>
            <tr style="background-color: #f8f9fa;">
                <th style="padding: 10px; border-bottom: 2px solid #dee2e6;">Mã đơn</th>
                <th style="padding: 10px; border-bottom: 2px solid #dee2e6;">Ngày đặt</th>
                <th style="padding: 10px; border-bottom: 2px solid #dee2e6;">Người nhận</th>
                <th style="padding: 10px; border-bottom: 2px solid #dee2e6;">SĐT</th>
                <th style="padding: 10px; border-bottom: 2px solid #dee2e6;">Trạng thái</th>
            </tr>
        </thead>
        <tbody>
            <c:choose>
                <c:when test="${empty orders}">
                    <tr>
                        <td colspan="5" style="padding: 20px; text-align: center; color: #6c757d;">Không có đơn hàng nào</td>
                    </tr>
                </c:when>
                <c:otherwise>
                    <c:forEach var="order" items="${orders}">
                        <tr>
                            <td style="padding: 10px; border-bottom: 1px solid #dee2e6;">#${order.orderId}</td>
                            <td style="padding: 10px; border-bottom: 1px solid #dee2e6;">
                                <fmt:formatDate value="${order.orderDate}" pattern="dd/MM/yyyy HH:mm"/>
                            </td>
                            <td style="padding: 10px; border-bottom: 1px solid #dee2e6;">${order.customerName}</td>
                            <td style="padding: 10px; border-bottom: 1px solid #dee2e6;">${order.phone}</td>
                            <td style="padding: 10px; border-bottom: 1px solid #dee2e6;">
                                <c:choose>
                                    <c:when test="${order.status == 0}"><span style="color: #007bff; font-weight: bold;">Đơn hàng mới</span></c:when>
                                    <c:when test="${order.status == 1}"><span style="color: #17a2b8; font-weight: bold;">Đã xác nhận</span></c:when>
                                    <c:when test="${order.status == 2}"><span style="color: #fd7e14; font-weight: bold;">Chuẩn bị hàng</span></c:when>
                                    <c:when test="${order.status == 3}"><span style="color: #6f42c1; font-weight: bold;">Vận chuyển</span></c:when>
                                    <c:when test="${order.status == 4}"><span style="color: #ffc107; font-weight: bold;">Giao hàng</span></c:when>
                                    <c:when test="${order.status == 5}"><span style="color: #28a745; font-weight: bold;">Đã giao</span></c:when>
                                    <c:when test="${order.status == 6}"><span style="color: #dc3545; font-weight: bold;">Đơn hàng hủy</span></c:when>
                                    <c:when test="${order.status == 7}"><span style="color: #6c757d; font-weight: bold;">Đơn hàng hoàn</span></c:when>
                                    <c:otherwise><span style="color: #6c757d; font-weight: bold;">Không xác định</span></c:otherwise>
                                </c:choose>
                            </td>
                        </tr>
                    </c:forEach>
                </c:otherwise>
            </c:choose>
        </tbody>
    </table>
</div>
