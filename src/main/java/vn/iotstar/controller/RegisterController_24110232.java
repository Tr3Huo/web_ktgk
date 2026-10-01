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
import vn.iotstar.util.EmailUtil_24110232;

@WebServlet(urlPatterns = {"/register"})
public class RegisterController_24110232 extends HttpServlet {
    IUserService_24110232 userService = new UserServiceImpl_24110232();

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        req.getRequestDispatcher("/views/web/register.jsp").forward(req, resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        req.setCharacterEncoding("UTF-8");
        resp.setCharacterEncoding("UTF-8");
        
        String username = req.getParameter("username");
        String fullname = req.getParameter("fullname");
        String email = req.getParameter("email");
        String password = req.getParameter("password");
        
        if (userService.findByUsername(username) != null) {
            req.setAttribute("message", "Tên đăng nhập đã tồn tại!");
            req.getRequestDispatcher("/views/web/register.jsp").forward(req, resp);
            return;
        }
        
        User_24110232 user = new User_24110232();
        user.setUsername(username);
        user.setFullname(fullname);
        user.setEmail(email);
        user.setPassword(password);
        user.setAdmin(false);
        user.setActive(false);
        
        userService.insert(user);
        
        String otp = EmailUtil_24110232.getRandomOTP();
        HttpSession session = req.getSession();
        session.setAttribute("otp", otp);
        session.setAttribute("username_otp", username);
        
        EmailUtil_24110232.sendEmail(email, otp);
        
        resp.sendRedirect(req.getContextPath() + "/verify-otp");
    }
}
