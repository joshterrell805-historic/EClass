package application;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;



public class ImportPromptController implements Initializable {
    @FXML //  fx:id="importYesButton"
    private Button importYesButton;
    @FXML //  fx:id="importNoButton"
    private Button importNoButton;

    @Override
    public void initialize(URL fxmlFileLocation, final ResourceBundle resources) {
    	importYesButton.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
            	Parent root = null;
            	try {
					root = FXMLLoader.load(getClass().getResource("ImportList.fxml"));
				} catch (IOException e) {
					e.printStackTrace();
				}
                Stage stage = new Stage();
                stage.setScene(new Scene(root, 285, 365));
                stage.show();
                ((Node)(event.getSource())).getScene().getWindow().hide();
            }		
    	});
    	importNoButton.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
            	((Node)(event.getSource())).getScene().getWindow().hide();
            }		
    	});
    }
}
