package vn.iotstar.controller;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import vn.iotstar.entity.User_24110232;
import vn.iotstar.service.IUserService_24110232;
import vn.iotstar.service.impl.UserServiceImpl_24110232;

@WebServlet(urlPatterns = {"/login"})
public class LoginController_24110232 extends HttpServlet {
    IUserService_24110232 userService = new UserServiceImpl_24110232();

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        req.getRequestDispatcher("/views/web/login.jsp").forward(req, resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        req.setCharacterEncoding("UTF-8");
        resp.setCharacterEncoding("UTF-8");
        
        String username = req.getParameter("username");
        String password = req.getParameter("password");
        
        User_24110232 user = userService.login(username, password);
        if (user != null) {
            if (user.getActive() == null || !user.getActive()) {
                req.setAttribute("message", "Tài khoản chưa được kích hoạt!");
                req.getRequestDispatcher("/views/web/login.jsp").forward(req, resp);
                return;
            }
            HttpSession session = req.getSession();
            session.setAttribute("account", user);
            
            if (user.getAdmin() != null && user.getAdmin()) {
                resp.sendRedirect(req.getContextPath() + "/admin/home");
            } else {
                resp.sendRedirect(req.getContextPath() + "/home");
            }
        } else {
            req.setAttribute("message", "Sai tài khoản hoặc mật khẩu!");
            req.getRequestDispatcher("/views/web/login.jsp").forward(req, resp);
        }
    }
}
