package vn.iotstar;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class FixData {
    public static void main(String[] args) {
        String url = "jdbc:sqlserver://localhost:1433;databaseName=KTGK_WEB;encrypt=true;trustServerCertificate=true";
        String user = "sa";
        String pass = "hung01634368089";
        
        try (Connection conn = DriverManager.getConnection(url, user, pass)) {
            String[] updates = {
                "UPDATE Category SET Categoryname = N'Giải trí' WHERE Categorycode = 'GIAITRI'",
                "UPDATE Category SET Categoryname = N'Học tập' WHERE Categorycode = 'HOCTAP'",
                "UPDATE Category SET Categoryname = N'Thể thao' WHERE Categorycode = 'THETHAO'",
                "UPDATE Videos SET Title = N'Video giải trí 1' WHERE VideoId = 'V01'",
                "UPDATE Videos SET Title = N'Video học tập 1' WHERE VideoId = 'V02'",
                "UPDATE Videos SET Title = N'Video thể thao 1' WHERE VideoId = 'V03'",
                "UPDATE Videos SET Title = N'Video giải trí 2' WHERE VideoId = 'V04'",
                "UPDATE Videos SET Title = N'Video học tập 2' WHERE VideoId = 'V05'",
                "UPDATE Videos SET Title = N'Video thể thao 2' WHERE VideoId = 'V06'",
                "UPDATE Videos SET Title = N'Video giải trí 3' WHERE VideoId = 'V07'",
                "UPDATE Videos SET Title = N'Video học tập 3' WHERE VideoId = 'V08'"
            };
            
            for (String sql : updates) {
                try (PreparedStatement ps = conn.prepareStatement(sql)) {
                    ps.executeUpdate();
                }
            }
            System.out.println("Data fixed successfully via JDBC.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
