import os

service_path = r'D:\Study\NAM3\KY1\DOT1\WEB\Workspace\Web_ktgk\src\main\java\vn\iotstar\service'
impl_path = os.path.join(service_path, 'impl')
if not os.path.exists(impl_path):
    os.makedirs(impl_path)

services = {
    'IUserService_24110232.java': """package vn.iotstar.service;

import vn.iotstar.entity.User_24110232;

public interface IUserService_24110232 {
    User_24110232 login(String username, String password);
    User_24110232 findByUsername(String username);
    void insert(User_24110232 user);
    void update(User_24110232 user);
}
""",
    'IVideoService_24110232.java': """package vn.iotstar.service;

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
""",
    'ICategoryService_24110232.java': """package vn.iotstar.service;

import java.util.List;
import vn.iotstar.entity.Category_24110232;

public interface ICategoryService_24110232 {
    List<Category_24110232> findAll();
    Category_24110232 findById(int categoryId);
}
""",
    'impl/UserServiceImpl_24110232.java': """package vn.iotstar.service.impl;

import vn.iotstar.dao.IUserDao_24110232;
import vn.iotstar.dao.impl.UserDaoImpl_24110232;
import vn.iotstar.entity.User_24110232;
import vn.iotstar.service.IUserService_24110232;

public class UserServiceImpl_24110232 implements IUserService_24110232 {

    IUserDao_24110232 userDao = new UserDaoImpl_24110232();

    @Override
    public User_24110232 login(String username, String password) {
        User_24110232 user = userDao.findByUsername(username);
        if (user != null && password.equals(user.getPassword())) {
            return user;
        }
        return null;
    }

    @Override
    public User_24110232 findByUsername(String username) {
        return userDao.findByUsername(username);
    }

    @Override
    public void insert(User_24110232 user) {
        userDao.insert(user);
    }

    @Override
    public void update(User_24110232 user) {
        userDao.update(user);
    }
}
""",
    'impl/VideoServiceImpl_24110232.java': """package vn.iotstar.service.impl;

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
""",
    'impl/CategoryServiceImpl_24110232.java': """package vn.iotstar.service.impl;

import java.util.List;
import vn.iotstar.dao.ICategoryDao_24110232;
import vn.iotstar.dao.impl.CategoryDaoImpl_24110232;
import vn.iotstar.entity.Category_24110232;
import vn.iotstar.service.ICategoryService_24110232;

public class CategoryServiceImpl_24110232 implements ICategoryService_24110232 {
    ICategoryDao_24110232 categoryDao = new CategoryDaoImpl_24110232();

    @Override
    public List<Category_24110232> findAll() {
        return categoryDao.findAll();
    }

    @Override
    public Category_24110232 findById(int categoryId) {
        return categoryDao.findById(categoryId);
    }
}
"""
}

for name, content in services.items():
    with open(os.path.join(service_path, name), 'w', encoding='utf-8') as f:
        f.write(content)

print("Services created.")
