package vn.iotstar.service.impl;

import java.util.List;
import vn.iotstar.dao.IVideoDao_24110232;
import vn.iotstar.dao.impl.VideoDaoImpl_24110232;
import vn.iotstar.entity.Video_24110232;
import vn.iotstar.service.IVideoService_24110232;

public class VideoServiceImpl_24110232 implements IVideoService_24110232 {

    IVideoDao_24110232 videoDao = new VideoDaoImpl_24110232();

    @Override
    public List<Video_24110232> findAll() {
        return videoDao.findAll();
    }

    @Override
    public List<Video_24110232> findAll(int page, int pagesize) {
        return videoDao.findAll(page, pagesize);
    }

    @Override
    public List<Video_24110232> findByCategory(int categoryId, int page, int pagesize) {
        return videoDao.findByCategory(categoryId, page, pagesize);
    }

    @Override
    public int count() {
        return videoDao.count();
    }

    @Override
    public int countByCategory(int categoryId) {
        return videoDao.countByCategory(categoryId);
    }

    @Override
    public Video_24110232 findById(String videoId) {
        return videoDao.findById(videoId);
    }

    @Override
    public void insert(Video_24110232 video) {
        videoDao.insert(video);
    }

    @Override
    public void update(Video_24110232 video) {
        videoDao.update(video);
    }

    @Override
    public void delete(String videoId) throws Exception {
        videoDao.delete(videoId);
    }
}
