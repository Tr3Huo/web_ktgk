package vn.iotstar.dao.impl;

import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;
import vn.iotstar.dao.IUserDao_24110232;
import vn.iotstar.entity.User_24110232;
import vn.iotstar.util.JPAConfig_24110232;

public class UserDaoImpl_24110232 implements IUserDao_24110232 {
    @Override
    public User_24110232 findByUsername(String username) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        return enma.find(User_24110232.class, username);
    }
    
    @Override
    public void insert(User_24110232 user) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        EntityTransaction trans = enma.getTransaction();
        try {
            trans.begin();
            enma.persist(user);
            trans.commit();
        } catch (Exception e) {
            e.printStackTrace();
            trans.rollback();
            throw e;
        } finally {
            enma.close();
        }
    }
    
    @Override
    public void update(User_24110232 user) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        EntityTransaction trans = enma.getTransaction();
        try {
            trans.begin();
            enma.merge(user);
            trans.commit();
        } catch (Exception e) {
            e.printStackTrace();
            trans.rollback();
            throw e;
        } finally {
            enma.close();
        }
    }
}
