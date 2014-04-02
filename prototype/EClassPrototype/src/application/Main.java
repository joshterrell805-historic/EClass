package application;
	
import java.util.logging.Level;
import java.util.logging.Logger;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.AnchorPane;

public class Main extends Application {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Application.launch(Main.class, (java.lang.String[])null);
    }

    @Override
    public void start(Stage primaryStage) {
        try {
        	// Show the whiteboard + navigation GUI
            AnchorPane page = (AnchorPane) FXMLLoader.load(Main.class.getResource("Login.fxml"));
        	// Uncomment to show the gear options and related GUIs
        	//AnchorPane page = (AnchorPane) FXMLLoader.load(Main.class.getResource("GearOptions.fxml"));
        	Scene scene = new Scene(page);
            primaryStage.setScene(scene);
            primaryStage.setTitle("Login");
            primaryStage.show();
            
        } catch (Exception ex) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
