package application;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;

public class AudioVideoController implements Initializable {
	@FXML //  fx:id="avOnButton"
	private Button avOnButton;
	@FXML //  fx:id="avOffButton"
	private Button avOffButton;
    
    @Override
    public void initialize(URL fxmlFileLocation, final ResourceBundle resources) {
    	
    	avOnButton.setOnAction(new EventHandler<ActionEvent>() {
    		@SuppressWarnings("unchecked")
			public void handle(ActionEvent event) {
				Parent root = null;
            	try {
					root = FXMLLoader.load(getClass().getResource("AudioVideoStream.fxml"));
				} catch (IOException e) {
					e.printStackTrace();
				}
                Stage stage = new Stage();
                stage.setScene(new Scene(root));
                stage.show();
            }		
    	});
    }
}