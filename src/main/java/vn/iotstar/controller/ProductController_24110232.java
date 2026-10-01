package vn.iotstar.controller;

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

@WebServlet(urlPatterns = {"/products"})
public class ProductController_24110232 extends HttpServlet {
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

        req.getRequestDispatcher("/views/web/products.jsp").forward(req, resp);
    }
}
