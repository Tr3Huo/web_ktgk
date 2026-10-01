package vn.iotstar.dao.impl;

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
