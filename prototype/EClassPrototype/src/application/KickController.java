package application;

import java.net.URL;
import java.util.ResourceBundle;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.control.Button;

public class KickController implements Initializable {
	@FXML
    private Button kickYesButton;
	@FXML
    private Button kickCancelButton;
	
    @Override
    public void initialize(URL fxmlFileLocation, final ResourceBundle resources) {
    	
    	kickYesButton.setOnAction(new EventHandler<ActionEvent>() {
    	    public void handle(ActionEvent e) {
    	    	((Node)(e.getSource())).getScene().getWindow().hide();
    	    }
    	});
    	
    	kickCancelButton.setOnAction(new EventHandler<ActionEvent>() {
    	    public void handle(ActionEvent e) {
    	    	((Node)(e.getSource())).getScene().getWindow().hide();
    	    }
    	});
    }
}

