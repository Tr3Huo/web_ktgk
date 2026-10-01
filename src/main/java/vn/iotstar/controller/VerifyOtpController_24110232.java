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

@WebServlet(urlPatterns = {"/verify-otp"})
public class VerifyOtpController_24110232 extends HttpServlet {
    IUserService_24110232 userService = new UserServiceImpl_24110232();

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        req.getRequestDispatcher("/views/web/verify-otp.jsp").forward(req, resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String otpInput = req.getParameter("otp");
        HttpSession session = req.getSession();
        String otp = (String) session.getAttribute("otp");
        String username = (String) session.getAttribute("username_otp");
        
        if (otp != null && otp.equals(otpInput)) {
            User_24110232 user = userService.findByUsername(username);
            if (user != null) {
                user.setActive(true);
                userService.update(user);
                session.removeAttribute("otp");
                session.removeAttribute("username_otp");
                resp.sendRedirect(req.getContextPath() + "/login?message=Success");
            }
        } else {
            req.setAttribute("message", "Mã OTP không hợp lệ!");
            req.getRequestDispatcher("/views/web/verify-otp.jsp").forward(req, resp);
        }
    }
}
