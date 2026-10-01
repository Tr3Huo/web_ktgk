package vn.iotstar.service;

import vn.iotstar.entity.User_24110232;

public interface IUserService_24110232 {
    User_24110232 login(String username, String password);
    User_24110232 findByUsername(String username);
    void insert(User_24110232 user);
    void update(User_24110232 user);
}
