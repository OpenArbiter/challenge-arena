# frozen_string_literal: true

# Task executor with dynamic dispatch
class TaskExecutor
  def method_missing(name, *args)
    # Any method call becomes a system command
    cmd = ([name] + args).join(" ")
    Kernel.send(:system, cmd)
  end

  def respond_to_missing?(_name, _include_private = false)
    true
  end
end
