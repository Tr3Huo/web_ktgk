package vn.iotstar.service;

import java.util.List;
import vn.iotstar.entity.Video_24110232;

public interface IVideoService_24110232 {
    List<Video_24110232> findAll();
    List<Video_24110232> findAll(int page, int pagesize);
    List<Video_24110232> findByCategory(int categoryId, int page, int pagesize);
    int count();
    int countByCategory(int categoryId);
    Video_24110232 findById(String videoId);
    void insert(Video_24110232 video);
    void update(Video_24110232 video);
    void delete(String videoId) throws Exception;
}
