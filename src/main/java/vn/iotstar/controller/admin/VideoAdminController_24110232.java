package vn.iotstar.controller.admin;

import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.List;
import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;
import vn.iotstar.entity.Category_24110232;
import vn.iotstar.entity.Video_24110232;
import vn.iotstar.service.ICategoryService_24110232;
import vn.iotstar.service.IVideoService_24110232;
import vn.iotstar.service.impl.CategoryServiceImpl_24110232;
import vn.iotstar.service.impl.VideoServiceImpl_24110232;

@MultipartConfig
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
        
        try {
            String videoId = req.getParameter("videoId");
            String title = req.getParameter("title");
            String description = req.getParameter("description");
            
            String poster = "";
            Part part = req.getPart("poster");
            if (part != null && part.getSize() > 0) {
                String fileName = Paths.get(part.getSubmittedFileName()).getFileName().toString();
                String uploadPath = req.getServletContext().getRealPath("/") + "uploads";
                File uploadDir = new File(uploadPath);
                if (!uploadDir.exists()) uploadDir.mkdir();
                part.write(uploadPath + File.separator + fileName);
                poster = req.getContextPath() + "/uploads/" + fileName;
            } else if (url.contains("/admin/video/edit")) {
                Video_24110232 oldVideo = videoService.findById(videoId);
                if (oldVideo != null) poster = oldVideo.getPoster();
            }
            
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
                if (videoService.findById(videoId) != null) {
                    req.setAttribute("message", "Lỗi: Video ID đã tồn tại!");
                    List<Category_24110232> categories = categoryService.findAll();
                    req.setAttribute("categories", categories);
                    req.getRequestDispatcher("/views/admin/video/add.jsp").forward(req, resp);
                    return;
                }
                videoService.insert(video);
                resp.sendRedirect(req.getContextPath() + "/admin/video");
            } else if (url.contains("/admin/video/edit")) {
                videoService.update(video);
                resp.sendRedirect(req.getContextPath() + "/admin/video");
            }
        } catch (Exception e) {
            e.printStackTrace();
            req.setAttribute("message", "Lỗi hệ thống: " + e.getMessage());
            req.getRequestDispatcher("/views/admin/video/list.jsp").forward(req, resp);
        }
    }
}
