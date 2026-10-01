package vn.iotstar.service.impl;

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
