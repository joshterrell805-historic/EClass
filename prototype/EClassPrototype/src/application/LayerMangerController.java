package application;

import java.io.IOException;
import java.net.URL;
import java.util.Observable;
import java.util.ResourceBundle;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Accordion;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.control.TitledPane;
import javafx.scene.control.ToolBar;
import javafx.stage.Stage;

public class LayerMangerController implements Initializable {
	@FXML //  fx:id="addButton"
	private Button addButton;
	@FXML //  fx:id="changeButton"
	private Button changeButton;
	@FXML //  fx:id="changeButton2"
	private Button changeButton2;
	@FXML //  fx:id="deleteButton"
	private Button deleteButton;
	@FXML //  fx:id="newLayer"
	private ToolBar newLayer;
    
    @Override
    public void initialize(URL fxmlFileLocation, final ResourceBundle resources) {
    	addButton.setOnAction(new EventHandler<ActionEvent>() {
			@SuppressWarnings("unchecked")
			public void handle(ActionEvent event) {
				Parent root = null;
            	try {
					root = FXMLLoader.load(getClass().getResource("AddMenu.fxml"));
				} catch (IOException e) {
					e.printStackTrace();
				}
                Stage stage = new Stage();
                stage.setScene(new Scene(root));
                stage.show();
                //((Node)(event.getSource())).getScene().getWindow().hide();
				newLayer.setVisible(true);
            }		
    	});
    	
    	changeButton.setOnAction(new EventHandler<ActionEvent>() {
			@SuppressWarnings("unchecked")
			public void handle(ActionEvent event) {
				Parent root = null;
            	try {
					root = FXMLLoader.load(getClass().getResource("ChangeMenu.fxml"));
				} catch (IOException e) {
					e.printStackTrace();
				}
                Stage stage = new Stage();
                stage.setScene(new Scene(root));
                stage.show();
            }		
    	});
    	
    	changeButton2.setOnAction(new EventHandler<ActionEvent>() {
			@SuppressWarnings("unchecked")
			public void handle(ActionEvent event) {
				Parent root = null;
            	try {
					root = FXMLLoader.load(getClass().getResource("ChangeMenu.fxml"));
				} catch (IOException e) {
					e.printStackTrace();
				}
                Stage stage = new Stage();
                stage.setScene(new Scene(root));
                stage.show();
				newLayer.setVisible(true);
            }		
    	});
    	
    	deleteButton.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
            	newLayer.setVisible(false);
            }		
    	});
    }

}
