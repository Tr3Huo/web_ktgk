package vn.iotstar.dao;

import vn.iotstar.entity.User_24110232;

public interface IUserDao_24110232 {
    User_24110232 findByUsername(String username);
    void insert(User_24110232 user);
    void update(User_24110232 user);
}
