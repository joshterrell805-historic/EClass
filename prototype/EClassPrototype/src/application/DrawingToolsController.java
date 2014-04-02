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
import javafx.scene.control.ContextMenu;
import javafx.scene.control.MenuBar;
import javafx.scene.control.MenuItem;
import javafx.scene.control.TitledPane;
import javafx.scene.control.ToggleButton;
import javafx.scene.control.ToggleGroup;
import javafx.scene.control.Tooltip;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;

public class DrawingToolsController implements Initializable {
	@FXML
	private ToggleButton ColorPallete;
	@FXML
	private ToggleButton PencilTool;
	@FXML
	private ToggleButton BasicShapesTool;
	@FXML
	private ToggleButton TextTool;
	@FXML
	private ToggleButton HandTool;
	@FXML
	private ToggleButton AttachmentTool;
	@FXML
	private TitledPane DrawingTools;
	@FXML
	private ContextMenu BasicShapes;
	@FXML
	private MenuItem BSCircle;
	@FXML
	private MenuItem BSSquare;
	@FXML
	private MenuItem BSTriangle;
	@FXML
	private MenuBar MenuBar;
	private ToggleGroup DrawingButtons;

	@Override
	public void initialize(URL fxmlFileLocation, final ResourceBundle resources) {
		// TODO Auto-generated method stub

		DrawingButtons = new ToggleGroup();
		PencilTool.setToggleGroup(DrawingButtons);
		BasicShapesTool.setToggleGroup(DrawingButtons);
		TextTool.setToggleGroup(DrawingButtons);
		HandTool.setToggleGroup(DrawingButtons);
		AttachmentTool.setToggleGroup(DrawingButtons);
		ColorPallete.setToggleGroup(DrawingButtons);

		ColorPallete.setOnAction(new EventHandler<ActionEvent>() {
			@SuppressWarnings("unchecked")
			public void handle(ActionEvent event) {
				Parent root = null;
            	try {
					root = FXMLLoader.load(getClass().getResource("ColorPallete.fxml"));
				} catch (IOException e) {
					e.printStackTrace();
				}
                Stage stage = new Stage();
                stage.setScene(new Scene(root));
                stage.show();
            }		
    	});

		PencilTool.setOnMouseEntered(new EventHandler<MouseEvent>() {

			@Override
			public void handle(MouseEvent event) {
				PencilTool.setTooltip(new Tooltip("Pencil"));
			}

		});
		PencilTool.setOnAction(new EventHandler<ActionEvent>() {

			@Override
			public void handle(ActionEvent event) {

			}

		});

		BasicShapesTool.setOnMouseEntered(new EventHandler<MouseEvent>() {

			@Override
			public void handle(MouseEvent event) {
				BasicShapesTool.setTooltip(new Tooltip(
						"Basic Shapes (Right-Click for shapes)"));
			}

		});
		BasicShapesTool.setOnAction(new EventHandler<ActionEvent>() {

			@Override
			public void handle(ActionEvent event) {

			}

		});

		TextTool.setOnMouseEntered(new EventHandler<MouseEvent>() {

			@Override
			public void handle(MouseEvent event) {
				TextTool.setTooltip(new Tooltip("Text"));
			}

		});
		TextTool.setOnAction(new EventHandler<ActionEvent>() {

			@Override
			public void handle(ActionEvent event) {

			}

		});

		HandTool.setOnMouseEntered(new EventHandler<MouseEvent>() {

			@Override
			public void handle(MouseEvent event) {
				HandTool.setTooltip(new Tooltip("Hand"));
			}

		});
		HandTool.setOnAction(new EventHandler<ActionEvent>() {

			@Override
			public void handle(ActionEvent event) {

			}

		});

		AttachmentTool.setOnMouseEntered(new EventHandler<MouseEvent>() {

			@Override
			public void handle(MouseEvent arg0) {
				// TODO Auto-generated method stub
				AttachmentTool.setTooltip(new Tooltip("Attachment"));
			}
		});
		AttachmentTool.setOnAction(new EventHandler<ActionEvent>() {

			@Override
			public void handle(ActionEvent event) {

			}

		});
	}
}
