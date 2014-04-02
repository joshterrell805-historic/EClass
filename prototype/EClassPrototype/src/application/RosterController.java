package application;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.geometry.Side;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ContextMenu;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.MenuItem;
import javafx.scene.control.TitledPane;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;


public class RosterController implements Initializable{

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private Label label1;

    @FXML
    private Label label2;

    @FXML
    private Label label3;

    @FXML
    private ListView<String> listViewInClass;

    @FXML
    private ListView<String> listViewRemoteAccess;

    @FXML
    private Rectangle rectange;

    @FXML
    private TitledPane titledPaneInClass;

    @FXML
    private TitledPane titledPaneRemoteAccess;
    
    @FXML
    private Button optionsButton;
	
    @FXML
	private ContextMenu optionsContextMenu;
	
    @FXML
	private MenuItem permissionsMenuItem;
	
    @FXML
	private MenuItem kickMenuItem;

    @Override
    public void initialize(URL fxmlFileLocation, final ResourceBundle resources) {
        ObservableList<String> inClass = FXCollections.observableArrayList(
    	 "Alek S.", "Brooke B.", "Charlotte W.", "Daniel B.", "Hayley L.",
    	 "John D.", "Lisa N.", "Nick G.", "Rachel G.", "Ryan G.", "Sam C.",
    	 "Taylor W.", "Tim A.", "Zach B.");
        ObservableList<String> remoteAccess = FXCollections.observableArrayList(
         "Carly A.", "Jane T.", "Kayla H.");
        listViewInClass.setItems(inClass);
        listViewRemoteAccess.setItems(remoteAccess);
        
        permissionsMenuItem.setOnAction(new EventHandler<ActionEvent>() {
    	    public void handle(ActionEvent e) {
    	    	Parent root = null;
            	try {
					root = FXMLLoader.load(getClass().getResource("PermissionsDialog.fxml"));
				} catch (IOException ex) {
					ex.printStackTrace();
				}
                Stage stage = new Stage();
                stage.setScene(new Scene(root));
                stage.show();
    	    }
    	});
    	
    	kickMenuItem.setOnAction(new EventHandler<ActionEvent>() {
    	    public void handle(ActionEvent e) {
    	    	Parent root = null;
            	try {
					root = FXMLLoader.load(getClass().getResource("KickDialog.fxml"));
				} catch (IOException ex) {
					ex.printStackTrace();
				}
                Stage stage = new Stage();
                stage.setScene(new Scene(root));
                stage.show();
    	    }
    	});
    	
    	optionsButton.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
            	optionsContextMenu.show(optionsButton, Side.RIGHT, 0, 0);
            }		
    	});
    }
}
