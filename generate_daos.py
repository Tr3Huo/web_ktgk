import os

dao_path = r'D:\Study\NAM3\KY1\DOT1\WEB\Workspace\Web_ktgk\src\main\java\vn\iotstar\dao'
impl_path = os.path.join(dao_path, 'impl')
if not os.path.exists(impl_path):
    os.makedirs(impl_path)

daos = {
    'IUserDao_24110232.java': """package vn.iotstar.dao;

import vn.iotstar.entity.User_24110232;

public interface IUserDao_24110232 {
    User_24110232 findByUsername(String username);
    void insert(User_24110232 user);
    void update(User_24110232 user);
}
""",
    'IVideoDao_24110232.java': """package vn.iotstar.dao;

import java.util.List;
import vn.iotstar.entity.Video_24110232;

public interface IVideoDao_24110232 {
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
    'ICategoryDao_24110232.java': """package vn.iotstar.dao;

import java.util.List;
import vn.iotstar.entity.Category_24110232;

public interface ICategoryDao_24110232 {
    List<Category_24110232> findAll();
    Category_24110232 findById(int categoryId);
}
""",
    'impl/UserDaoImpl_24110232.java': """package vn.iotstar.dao.impl;

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
""",
    'impl/VideoDaoImpl_24110232.java': """package vn.iotstar.dao.impl;

import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;
import javax.persistence.Query;
import javax.persistence.TypedQuery;
import vn.iotstar.dao.IVideoDao_24110232;
import vn.iotstar.entity.Video_24110232;
import vn.iotstar.util.JPAConfig_24110232;

public class VideoDaoImpl_24110232 implements IVideoDao_24110232 {

    @Override
    public List<Video_24110232> findAll() {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        TypedQuery<Video_24110232> query = enma.createQuery("SELECT v FROM Video_24110232 v", Video_24110232.class);
        return query.getResultList();
    }

    @Override
    public List<Video_24110232> findAll(int page, int pagesize) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        TypedQuery<Video_24110232> query = enma.createQuery("SELECT v FROM Video_24110232 v", Video_24110232.class);
        query.setFirstResult(page * pagesize);
        query.setMaxResults(pagesize);
        return query.getResultList();
    }

    @Override
    public List<Video_24110232> findByCategory(int categoryId, int page, int pagesize) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        TypedQuery<Video_24110232> query = enma.createQuery("SELECT v FROM Video_24110232 v WHERE v.category.categoryId = :catId", Video_24110232.class);
        query.setParameter("catId", categoryId);
        query.setFirstResult(page * pagesize);
        query.setMaxResults(pagesize);
        return query.getResultList();
    }

    @Override
    public int count() {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        String jpql = "SELECT count(v) FROM Video_24110232 v";
        Query query = enma.createQuery(jpql);
        return ((Long) query.getSingleResult()).intValue();
    }

    @Override
    public int countByCategory(int categoryId) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        String jpql = "SELECT count(v) FROM Video_24110232 v WHERE v.category.categoryId = :catId";
        Query query = enma.createQuery(jpql);
        query.setParameter("catId", categoryId);
        return ((Long) query.getSingleResult()).intValue();
    }

    @Override
    public Video_24110232 findById(String videoId) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        return enma.find(Video_24110232.class, videoId);
    }

    @Override
    public void insert(Video_24110232 video) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        EntityTransaction trans = enma.getTransaction();
        try {
            trans.begin();
            enma.persist(video);
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
    public void update(Video_24110232 video) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        EntityTransaction trans = enma.getTransaction();
        try {
            trans.begin();
            enma.merge(video);
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
    public void delete(String videoId) throws Exception {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        EntityTransaction trans = enma.getTransaction();
        try {
            trans.begin();
            Video_24110232 video = enma.find(Video_24110232.class, videoId);
            if (video != null) {
                enma.remove(video);
            } else {
                throw new Exception("Not found");
            }
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
""",
    'impl/CategoryDaoImpl_24110232.java': """package vn.iotstar.dao.impl;

import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.TypedQuery;
import vn.iotstar.dao.ICategoryDao_24110232;
import vn.iotstar.entity.Category_24110232;
import vn.iotstar.util.JPAConfig_24110232;

public class CategoryDaoImpl_24110232 implements ICategoryDao_24110232 {
    @Override
    public List<Category_24110232> findAll() {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        TypedQuery<Category_24110232> query = enma.createQuery("SELECT c FROM Category_24110232 c", Category_24110232.class);
        return query.getResultList();
    }
    
    @Override
    public Category_24110232 findById(int categoryId) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        return enma.find(Category_24110232.class, categoryId);
    }
}
"""
}

for name, content in daos.items():
    with open(os.path.join(dao_path, name), 'w', encoding='utf-8') as f:
        f.write(content)

print("DAOs created.")
