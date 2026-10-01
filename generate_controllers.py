import os

controller_path = r'D:\Study\NAM3\KY1\DOT1\WEB\Workspace\Web_ktgk\src\main\java\vn\iotstar\controller'
admin_path = os.path.join(controller_path, 'admin')

controllers = {
    'LoginController_24110232.java': """package vn.iotstar.controller;

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
""",
    'LogoutController_24110232.java': """package vn.iotstar.controller;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet(urlPatterns = {"/logout"})
public class LogoutController_24110232 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        HttpSession session = req.getSession();
        session.removeAttribute("account");
        resp.sendRedirect(req.getContextPath() + "/login");
    }
}
""",
    'RegisterController_24110232.java': """package vn.iotstar.controller;

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
""",
    'VerifyOtpController_24110232.java': """package vn.iotstar.controller;

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
""",
    'HomeController_24110232.java': """package vn.iotstar.controller;

import java.io.IOException;
import java.util.List;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import vn.iotstar.entity.Category_24110232;
import vn.iotstar.entity.Video_24110232;
import vn.iotstar.service.ICategoryService_24110232;
import vn.iotstar.service.IVideoService_24110232;
import vn.iotstar.service.impl.CategoryServiceImpl_24110232;
import vn.iotstar.service.impl.VideoServiceImpl_24110232;

@WebServlet(urlPatterns = {"/home"})
public class HomeController_24110232 extends HttpServlet {
    ICategoryService_24110232 categoryService = new CategoryServiceImpl_24110232();
    IVideoService_24110232 videoService = new VideoServiceImpl_24110232();

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String catIdStr = req.getParameter("catId");
        String pageStr = req.getParameter("page");
        int page = (pageStr != null) ? Integer.parseInt(pageStr) - 1 : 0;
        int pageSize = 3;

        List<Category_24110232> categories = categoryService.findAll();
        req.setAttribute("categories", categories);

        if (catIdStr != null) {
            int catId = Integer.parseInt(catIdStr);
            List<Video_24110232> videos = videoService.findByCategory(catId, page, pageSize);
            int count = videoService.countByCategory(catId);
            int endPage = count / pageSize;
            if (count % pageSize != 0) {
                endPage++;
            }
            req.setAttribute("videos", videos);
            req.setAttribute("endPage", endPage);
            req.setAttribute("catId", catId);
            req.setAttribute("count", count);
        } else {
            // default load first category or all videos
            if (categories.size() > 0) {
                int catId = categories.get(0).getCategoryId();
                List<Video_24110232> videos = videoService.findByCategory(catId, page, pageSize);
                int count = videoService.countByCategory(catId);
                int endPage = count / pageSize;
                if (count % pageSize != 0) {
                    endPage++;
                }
                req.setAttribute("videos", videos);
                req.setAttribute("endPage", endPage);
                req.setAttribute("catId", catId);
                req.setAttribute("count", count);
            }
        }
        
        req.getRequestDispatcher("/views/web/home.jsp").forward(req, resp);
    }
}
""",
    'VideoDetailController_24110232.java': """package vn.iotstar.controller;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import vn.iotstar.entity.Video_24110232;
import vn.iotstar.service.IVideoService_24110232;
import vn.iotstar.service.impl.VideoServiceImpl_24110232;

@WebServlet(urlPatterns = {"/video-detail"})
public class VideoDetailController_24110232 extends HttpServlet {
    IVideoService_24110232 videoService = new VideoServiceImpl_24110232();

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String videoId = req.getParameter("id");
        Video_24110232 video = videoService.findById(videoId);
        req.setAttribute("video", video);
        
        req.getRequestDispatcher("/views/web/video-detail.jsp").forward(req, resp);
    }
}
""",
    'admin/AdminHomeController_24110232.java': """package vn.iotstar.controller.admin;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(urlPatterns = {"/admin/home"})
public class AdminHomeController_24110232 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        req.getRequestDispatcher("/views/admin/home.jsp").forward(req, resp);
    }
}
""",
    'admin/VideoAdminController_24110232.java': """package vn.iotstar.controller.admin;

import java.io.IOException;
import java.util.List;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import vn.iotstar.entity.Category_24110232;
import vn.iotstar.entity.Video_24110232;
import vn.iotstar.service.ICategoryService_24110232;
import vn.iotstar.service.IVideoService_24110232;
import vn.iotstar.service.impl.CategoryServiceImpl_24110232;
import vn.iotstar.service.impl.VideoServiceImpl_24110232;

@WebServlet(urlPatterns = {"/admin/video", "/admin/video/add", "/admin/video/edit", "/admin/video/delete"})
public class VideoAdminController_24110232 extends HttpServlet {
    IVideoService_24110232 videoService = new VideoServiceImpl_24110232();
    ICategoryService_24110232 categoryService = new CategoryServiceImpl_24110232();

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String url = req.getRequestURL().toString();
        req.setCharacterEncoding("UTF-8");
        resp.setCharacterEncoding("UTF-8");
        
        if (url.contains("/admin/video/add")) {
            List<Category_24110232> categories = categoryService.findAll();
            req.setAttribute("categories", categories);
            req.getRequestDispatcher("/views/admin/video/add.jsp").forward(req, resp);
        } else if (url.contains("/admin/video/edit")) {
            String id = req.getParameter("id");
            Video_24110232 video = videoService.findById(id);
            List<Category_24110232> categories = categoryService.findAll();
            req.setAttribute("categories", categories);
            req.setAttribute("video", video);
            req.getRequestDispatcher("/views/admin/video/edit.jsp").forward(req, resp);
        } else if (url.contains("/admin/video/delete")) {
            String id = req.getParameter("id");
            try {
                videoService.delete(id);
                req.setAttribute("message", "Xóa thành công!");
            } catch (Exception e) {
                req.setAttribute("message", "Lỗi: " + e.getMessage());
            }
            resp.sendRedirect(req.getContextPath() + "/admin/video");
        } else {
            String pageStr = req.getParameter("page");
            int page = (pageStr != null) ? Integer.parseInt(pageStr) - 1 : 0;
            int pageSize = 6;
            
            List<Video_24110232> videos = videoService.findAll(page, pageSize);
            int count = videoService.count();
            int endPage = count / pageSize;
            if (count % pageSize != 0) {
                endPage++;
            }
            
            req.setAttribute("videos", videos);
            req.setAttribute("endPage", endPage);
            req.getRequestDispatcher("/views/admin/video/list.jsp").forward(req, resp);
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String url = req.getRequestURL().toString();
        req.setCharacterEncoding("UTF-8");
        resp.setCharacterEncoding("UTF-8");
        
        String videoId = req.getParameter("videoId");
        String title = req.getParameter("title");
        String description = req.getParameter("description");
        String poster = req.getParameter("poster");
        String viewsStr = req.getParameter("views");
        int views = (viewsStr != null && !viewsStr.isEmpty()) ? Integer.parseInt(viewsStr) : 0;
        String activeStr = req.getParameter("active");
        Boolean active = (activeStr != null && activeStr.equals("true"));
        String catIdStr = req.getParameter("categoryId");
        int categoryId = Integer.parseInt(catIdStr);
        
        Category_24110232 category = categoryService.findById(categoryId);
        Video_24110232 video = new Video_24110232();
        video.setVideoId(videoId);
        video.setTitle(title);
        video.setDescription(description);
        video.setPoster(poster);
        video.setViews(views);
        video.setActive(active);
        video.setCategory(category);
        
        if (url.contains("/admin/video/add")) {
            videoService.insert(video);
            resp.sendRedirect(req.getContextPath() + "/admin/video");
        } else if (url.contains("/admin/video/edit")) {
            videoService.update(video);
            resp.sendRedirect(req.getContextPath() + "/admin/video");
        }
    }
}
"""
}

for name, content in controllers.items():
    if '/' in name:
        with open(os.path.join(controller_path, name), 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        with open(os.path.join(controller_path, name), 'w', encoding='utf-8') as f:
            f.write(content)

print("Controllers created.")
