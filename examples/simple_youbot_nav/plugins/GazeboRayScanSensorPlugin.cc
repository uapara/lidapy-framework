#include "GazeboRayScanSensorPlugin.hh"

using namespace gazebo;
GZ_REGISTER_SENSOR_PLUGIN(GazeboRayScanSensorPlugin)

GazeboRayScanSensorPlugin::GazeboRayScanSensorPlugin() : SensorPlugin()
{
    topicName = "/gazebo/sensors/rayscan";
}

GazeboRayScanSensorPlugin::~GazeboRayScanSensorPlugin()
{
}

void GazeboRayScanSensorPlugin::InitPublisher()
{
    ros::NodeHandle nh;

    this->publisher
        = nh.advertise<simple_youbot_nav::RayScanSensor>(
              this->topicName, 1000);

    ROS_INFO_STREAM("RayScanPlugin reporting for duty!");
}

void GazeboRayScanSensorPlugin::Load(sensors::SensorPtr _sensor, sdf::ElementPtr /*_sdf*/)
{
    this->parentSensor =
        boost::dynamic_pointer_cast<sensors::RaySensor>(_sensor);

    if (!this->parentSensor)
    {
        ROS_FATAL_STREAM("RayScanPlugin requires a RaySensor.  Unable to load plugin.");
        return;
    }

    this->updateConnection = this->parentSensor->ConnectUpdated(
                                 boost::bind(&GazeboRayScanSensorPlugin::OnUpdate, this));

    InitPublisher();

    this->parentSensor->SetActive(true);
}

void GazeboRayScanSensorPlugin::OnUpdate()
{
    simple_youbot_nav::RayScanSensor msg;

    getRanges(msg);
    publish(msg);
}

void GazeboRayScanSensorPlugin::getRanges(simple_youbot_nav::RayScanSensor& msg)
{
    this->parentSensor->SetActive(false);
    for (int i = 0; i < this->parentSensor->GetRangeCount(); ++i)
    {
        msg.ranges.push_back(this->parentSensor->GetRange(i));
    }
    this->parentSensor->SetActive(true);
}

void GazeboRayScanSensorPlugin::publish(simple_youbot_nav::RayScanSensor& msg)
{
    if (ros::ok()) {
        this->publisher.publish(msg);
    }
}
