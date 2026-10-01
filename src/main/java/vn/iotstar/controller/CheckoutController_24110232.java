package vn.iotstar.controller;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Map;
import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import vn.iotstar.entity.Order_24110232;
import vn.iotstar.entity.OrderDetail_24110232;
import vn.iotstar.model.CartItem;
import vn.iotstar.util.JPAConfig_24110232;

@WebServlet(urlPatterns = {"/checkout"})
public class CheckoutController_24110232 extends HttpServlet {
    private static final long serialVersionUID = 1L;

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        HttpSession session = req.getSession();
        Map<String, CartItem> cart = (Map<String, CartItem>) session.getAttribute("cart");
        
        if (cart == null || cart.isEmpty()) {
            resp.sendRedirect(req.getContextPath() + "/cart");
            return;
        }
        
        req.getRequestDispatcher("/views/web/checkout.jsp").forward(req, resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        req.setCharacterEncoding("UTF-8");
        HttpSession session = req.getSession();
        Map<String, CartItem> cart = (Map<String, CartItem>) session.getAttribute("cart");
        
        if (cart == null || cart.isEmpty()) {
            resp.sendRedirect(req.getContextPath() + "/cart");
            return;
        }

        String customerName = req.getParameter("customerName");
        String phone = req.getParameter("phone");
        String address = req.getParameter("address");
        String paymentMethod = req.getParameter("paymentMethod"); // e.g., COD
        
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        EntityTransaction trans = enma.getTransaction();
        
        try {
            trans.begin();
            
            Order_24110232 order = new Order_24110232();
            order.setCustomerName(customerName);
            order.setPhone(phone);
            order.setAddress(address);
            order.setPaymentMethod(paymentMethod);
            order.setOrderDate(new Date());
            order.setStatus(0); // Pending
            
            List<OrderDetail_24110232> details = new ArrayList<>();
            for (CartItem item : cart.values()) {
                OrderDetail_24110232 detail = new OrderDetail_24110232();
                detail.setOrder(order);
                detail.setVideo(item.getVideo());
                detail.setQuantity(item.getQuantity());
                details.add(detail);
            }
            order.setOrderDetails(details);
            
            enma.persist(order);
            trans.commit();
            
            // Clear cart
            session.removeAttribute("cart");
            
            req.setAttribute("message", "Thanh toán thành công! Mã đơn hàng của bạn là: " + order.getOrderId());
            req.getRequestDispatcher("/views/web/checkout-success.jsp").forward(req, resp);
            
        } catch (Exception e) {
            e.printStackTrace();
            trans.rollback();
            req.setAttribute("error", "Có lỗi xảy ra trong quá trình thanh toán!");
            req.getRequestDispatcher("/views/web/checkout.jsp").forward(req, resp);
        } finally {
            enma.close();
        }
    }
}
