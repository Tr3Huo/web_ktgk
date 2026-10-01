package vn.iotstar.controller;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import vn.iotstar.entity.Video_24110232;
import vn.iotstar.model.CartItem;
import vn.iotstar.service.IVideoService_24110232;
import vn.iotstar.service.impl.VideoServiceImpl_24110232;

@WebServlet(urlPatterns = {"/cart", "/cart/add", "/cart/remove", "/cart/update"})
public class CartController_24110232 extends HttpServlet {
    private static final long serialVersionUID = 1L;
    private IVideoService_24110232 videoService = new VideoServiceImpl_24110232();

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String path = req.getServletPath();
        if ("/cart".equals(path)) {
            req.getRequestDispatcher("/views/web/cart.jsp").forward(req, resp);
        } else {
            handleCartAction(req, resp);
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        handleCartAction(req, resp);
    }

    @SuppressWarnings("unchecked")
    private void handleCartAction(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        String path = req.getServletPath();
        String videoId = req.getParameter("videoId");
        
        HttpSession session = req.getSession();
        Map<String, CartItem> cart = (Map<String, CartItem>) session.getAttribute("cart");
        if (cart == null) {
            cart = new HashMap<>();
        }

        if (videoId != null && !videoId.isEmpty()) {
            if ("/cart/add".equals(path)) {
                if (cart.containsKey(videoId)) {
                    CartItem item = cart.get(videoId);
                    int newQty = item.getQuantity() + 1;
                    if (newQty > 100) newQty = 100; // Limit
                    item.setQuantity(newQty);
                } else {
                    Video_24110232 video = videoService.findById(videoId);
                    if (video != null) {
                        cart.put(videoId, new CartItem(video, 1));
                    }
                }
            } else if ("/cart/remove".equals(path)) {
                cart.remove(videoId);
            } else if ("/cart/update".equals(path)) {
                try {
                    int quantity = Integer.parseInt(req.getParameter("quantity"));
                    if (quantity < 1) quantity = 1;
                    if (quantity > 100) quantity = 100; // Limit
                    
                    if (cart.containsKey(videoId)) {
                        cart.get(videoId).setQuantity(quantity);
                    }
                } catch (NumberFormatException e) {
                    // Ignore invalid quantity
                }
            }
        }
        
        session.setAttribute("cart", cart);
        
        // Redirect back to cart page or previous page
        String referer = req.getHeader("Referer");
        if ("/cart/add".equals(path) && referer != null) {
            resp.sendRedirect(referer);
        } else {
            resp.sendRedirect(req.getContextPath() + "/cart");
        }
    }
}
