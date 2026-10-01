package vn.iotstar.controller;

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
