package application;

import javafx.fxml.FXML;
import javafx.scene.chart.ScatterChart;
import javafx.scene.control.ScrollBar;
import javafx.scene.layout.AnchorPane;
import javafx.scene.text.Text;

public class ApprovalTrackerAnalysisController {
	@FXML
	private AnchorPane ApprovalTrackerAnalysis;
	@FXML
	private ScatterChart ATAChart;
	@FXML
	private Text ATADataPointVal;
	@FXML
	private Text ATAApprovalVal;
	@FXML
	private Text ATASlideNoVal;
	@FXML
	private Text ATATimeOnSlideVal;
	@FXML
	private ScrollBar ATAScrollBar;
}
