package vn.iotstar.service.impl;

import java.util.List;
import vn.iotstar.dao.IOrderDao_24110232;
import vn.iotstar.dao.impl.OrderDaoImpl_24110232;
import vn.iotstar.entity.Order_24110232;
import vn.iotstar.service.IOrderService_24110232;

public class OrderServiceImpl_24110232 implements IOrderService_24110232 {
    
    IOrderDao_24110232 orderDao = new OrderDaoImpl_24110232();

    @Override
    public List<Order_24110232> findAll() {
        return orderDao.findAll();
    }

    @Override
    public List<Order_24110232> findByPhone(String phone) {
        return orderDao.findByPhone(phone);
    }

    @Override
    public List<Order_24110232> findByPhoneAndStatus(String phone, int status) {
        return orderDao.findByPhoneAndStatus(phone, status);
    }

    @Override
    public List<Order_24110232> findByUser(String username) {
        return orderDao.findByUser(username);
    }

    @Override
    public List<Order_24110232> findByUserAndStatus(String username, int status) {
        return orderDao.findByUserAndStatus(username, status);
    }

    @Override
    public Order_24110232 findById(int id) {
        return orderDao.findById(id);
    }

    @Override
    public void updateStatus(int orderId, int status) {
        orderDao.updateStatus(orderId, status);
    }
}
