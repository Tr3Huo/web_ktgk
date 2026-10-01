package vn.iotstar.controller;

import java.io.IOException;
import java.util.List;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import vn.iotstar.entity.Order_24110232;
import vn.iotstar.entity.User_24110232;
import vn.iotstar.service.IOrderService_24110232;
import vn.iotstar.service.impl.OrderServiceImpl_24110232;

@WebServlet(urlPatterns = {"/orders"})
public class OrderHistoryController_24110232 extends HttpServlet {
    private static final long serialVersionUID = 1L;
    
    IOrderService_24110232 orderService = new OrderServiceImpl_24110232();

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        HttpSession session = req.getSession();
        User_24110232 user = (User_24110232) session.getAttribute("account");
        
        if (user == null) {
            resp.sendRedirect(req.getContextPath() + "/login");
            return;
        }
        
        String statusStr = req.getParameter("status");
        List<Order_24110232> orders = null;
        
        if (statusStr != null && !statusStr.isEmpty()) {
            try {
                int status = Integer.parseInt(statusStr);
                orders = orderService.findByUserAndStatus(user.getUsername(), status);
                req.setAttribute("currentStatus", status);
            } catch (NumberFormatException e) {
                orders = orderService.findByUser(user.getUsername());
            }
        } else {
            orders = orderService.findByUser(user.getUsername());
        }
        
        req.setAttribute("orders", orders);
        req.getRequestDispatcher("/views/web/order-history.jsp").forward(req, resp);
    }
}
